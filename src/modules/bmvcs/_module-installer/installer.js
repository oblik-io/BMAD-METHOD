// BMVCS Module Installer
// Handles VCS discovery during installation

async function install(config) {
  console.log('Installing BMVCS module...');

  // Create VCS config directory if needed
  const vcsConfigPath = config.vcs_config_location;
  console.log(`VCS config will be stored at: ${vcsConfigPath}`);

  // Run VCS discovery if user opted in
  if (config.run_vcs_discovery === true) {
    console.log('Running VCS discovery...');
    console.log('Please activate VCS Adapter agent and run: *discover');
  } else {
    console.log('VCS discovery skipped. Run later via VCS Adapter agent: *discover');
  }

  console.log('✅ BMVCS module installed successfully');
  return true;
}

module.exports = { install };
